node {
    checkout scm
    def testImage = docker.build("test-image", ".") 

    testImage.inside {
        sh './manage.py test openweathermap'
    }

    stage name: 'TF Plan' 
       sh '/home/alex/softserve/docker_work/terraform init terraform/'
       sh '/home/alex/softserve/docker_work/terraform plan terrform/'
 }
