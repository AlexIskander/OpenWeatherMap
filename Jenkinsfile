node {
    checkout scm
    def testImage = docker.build("test-image", "./OpenWeatherMap/Dockerfile") 

    testImage.inside {
        sh 'make test'
    }
}
