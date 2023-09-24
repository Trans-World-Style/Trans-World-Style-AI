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
                    role: kanikoBuild
                spec:
                  containers:
                  - name: kaniko
                    image: gcr.io/kaniko-project/executor:latest
                    args: ["--context=dir://workspace", "--dockerfile=Dockerfile", "--destination=${DOCKERHUB_USER}/tws-ai:latest"]
                    volumeMounts:
                      - mountPath: "/kaniko/.docker/"
                        name: "docker-config"
                  volumes:
                    - name: docker-config
                      emptyDir: {}  // 일시적인 저장 공간을 제공
                """
        }
    }
    stages {
        stage('Build and Push') {
            steps {
                container('kaniko') {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                        script {
                            sh """
                                echo '{ "auths": { "https://index.docker.io/v1/": { "auth": "$DOCKERHUB_USER:$DOCKERHUB_PASS" } } }' > /kaniko/.docker/config.json
                            """
                            // 이미지 빌드 및 푸시
                            sh "/kaniko/executor --context dir://workspace --dockerfile=Dockerfile --destination=${DOCKERHUB_USER}/tws-ai:latest"
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
