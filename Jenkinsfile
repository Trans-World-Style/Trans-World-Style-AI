pipeline {
    agent any
    stages {
        stage('Setup and Deploy') {
            when {
                anyOf {
                    branch 'main'
                }
            }
            steps {
                script {
                    sh """
                        echo 'test run!!!!'
                    """
                    withKubeConfig([credentialsId: jenkins-admin]) {
                        sh 'kubectl get nodes -n prod'
                    }
                }
            }
        }
    }
}

// pipeline {
//     agent any
//     environment {
//         DOCKER_TAG = ''
//     }
//     stages {
//         stage('Extract Docker Tag') {
//             steps {
//                 script {
//                     def match = params.commit_message =~ /tag: (\S+)/
//                     if(match) {
//                         env.DOCKER_TAG = match[0][1]
//                     } else {
//                         error("Tag not found in commit message!")
//                     }
//                 }
//             }
//         }
//
//         stage('Build and Push Docker Image') {
//             steps {
//                 script {
//                     if(env.DOCKER_TAG) {
//                         // Docker 빌드 및 푸시
//                         sh "docker build -t myimage:${env.DOCKER_TAG} ."
//                         sh "docker push myimage:${env.DOCKER_TAG}"
//                     } else {
//                         error("Docker tag is empty!")
//                     }
//                 }
//             }
//         }
//     }
// }
