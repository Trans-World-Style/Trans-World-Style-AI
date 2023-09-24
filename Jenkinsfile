pipeline {
    agent any
    stages {
        stage('Build') {
            when {
                anyOf {
                    branch 'main'
                }
            }
            steps {
                script {
                    sh """
                        docker build --platform=linux/amd64 -t dodo133/tws-ai .
                    """
                    sh """
                        docker push dodo133/tws-ai
                    """
//                     withKubeConfig([namespace: "prod"]) {
//                         sh 'kubectl get po'
//                     }
                }
            }
        }
    }
}

// pull & build & push

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
