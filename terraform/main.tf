provider "aws" {
  region = "eu-central-1"
  shared_credentials_file = "/opt/projects/aws/credentials"
}

resource "aws_instance" "example" {
  ami = "ami-0f5dbc86dd9cbf7a8"
  instance_type = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.instance.id}"]
  key_name = "${aws_key_pair.work_key.key_name}"

  user_data = <<-EOF
              #!/bin/bash
              yum install git -y
              yum install python-pip -y
              mkdir /var/www/
              git clone https://github.com/AlexIskander/OpenWeatherMap
              cd OpenWeatherMap
              pip install -r requirements.txt
              python manage.py migrate   
              nohup python manage.py runserver 0.0.0.0:"${var.server_port}" &
              EOF

  tags {
    name = "terraform-example"
  }
}

resource "aws_security_group" "instance" {
  name = "terraform-example-instance"
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
}
}

resource "aws_key_pair" "work_key" {
  key_name   = "work_key"
  public_key = "${file("/opt/projects/keys/my_key.pub")}"
}

output "public_ip" {
  value = "${aws_instance.example.public_ip}"
}

variable "server_port" {
  description = "The port the server will use for HTTP requests"
  default = 8888
}
