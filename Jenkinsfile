pipeline {
    agent {
        kubernetes {
            cloud "kubernetes-docker-job"
            yaml """
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                role: kanikoBuild
            spec:
              containers:
              - name: kaniko
                image: gcr.io/kaniko-project/executor:latest
                args:
                - "--dockerfile=${WORKSPACE}/Dockerfile"
                - "--context=dir://${WORKSPACE}/"
                - "--destination=dodo133/tws-ai:latest"
                env:
                - name: DOCKER_CONFIG
                  value: "/kaniko/.docker/"
                volumeMounts:
                - name: docker-config
                  mountPath: /kaniko/.docker/
              volumes:
              - name: docker-config
                projected:
                  sources:
                  - secret:
                      name: dockerhub-secret
                      items:
                        - key: .dockerconfigjson
                          path: config.json
            """
        }
    }
    stages {
        stage('Build and Push Image') {
            steps {
                script {
                    // Dockerfile을 사용하여 이미지를 빌드하고 Docker Hub에 푸시
                    container('kaniko') {
                        sh """
                        /kaniko/executor
                        """
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
