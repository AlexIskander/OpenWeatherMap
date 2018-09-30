pipeline {
   agent {
       docker {
           image 'ubuntu:latest'
       }
   }
   stages {
       stage('checkout'){
           steps {
               checkout scm
           }
       }
       stage('build'){
           steps {
               echo 'build'
               }
        }
        stage('deploy'){
            steps{
                echo 'deploy'
                sh 'ls -l'
            }
        }
   }
}
