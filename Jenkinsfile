node {
    checkout scm
    def testImage = docker.build("test-image", ".") 

    testImage.inside {
        sh './manage.py test openweathermap'
    }

    stage name: 'Plan and Deploy'
       sh "./prepare-infra.sh" 
 }
