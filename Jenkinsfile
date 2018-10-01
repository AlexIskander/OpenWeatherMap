node {
    checkout scm
    def testImage = docker.build("test-image", ".") 

    testImage.inside {
        sh './manage.py test openweathermap'
    }

    stage name: 'TF Plan'
       sh "prepare-infra.sh" 
 }
