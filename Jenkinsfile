pipeline {
    agent {
        kubernetes {
            cloud "kubernetes-docker-job"
            yaml """
                apiVersion: v1
                kind: Pod
                metadata:
                  namespace: jenkins
                  labels:
                    role: dockerBuildPush
                spec:
                  containers:
                  - name: docker
                    image: docker:20.10-dind
                    command: ["dockerd"]
                    args: ["--host=unix:///var/run/docker.sock", "--host=tcp://0.0.0.0:2375"]
                  securityContext:
                    privileged: true
                """
        }
    }
    environment {
        DOCKERHUB_USER = 'dodo133'
//         DOCKERHUB_PASS = 'kay24125@'
    }
    stages {
        stage('Build and Push') {
            steps {
                container('docker') {
                    script {
                        def dockerImage = docker.build("${DOCKERHUB_USER}/tws-ai")
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                            dockerImage.push('latest')
                        }
                    }
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
