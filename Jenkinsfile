node {
    checkout scm
    def testImage = docker.build("test-image", ".") 

    runImage.inside {
        sh 'make run'
    }
}
