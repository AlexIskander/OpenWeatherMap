node {
    checkout scm
    def testImage = docker.build("test-image", "./Dockerfile") 

    testImage.inside {
        sh 'make test'
    }
}
