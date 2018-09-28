pipeline {
   agent {
       docker {
           image 'ubuntu:latest'
       }
   }
   stages {
       stage('checkout'){
           steps {
               checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/AlexIskander/OpenWeatherMap']]])
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
