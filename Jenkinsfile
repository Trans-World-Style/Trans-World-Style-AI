// pipeline {
//     agent {
//         kubernetes {
//             cloud "kubernetes-docker-job"
//             yaml """
//             apiVersion: v1
//             kind: Pod
//             metadata:
//               labels:
//                 role: kanikoBuild
//             spec:
//               containers:
//               - name: kaniko
//                 image: gcr.io/kaniko-project/executor:latest
//                 volumeMounts:
//                   - name: dockerhub-secret
//                     mountPath: /secret/
//                     readOnly: true
//               volumes:
//               - name: dockerhub-secret
//                 secret:
//                   secretName: dockerhub-secret
//             """
//         }
//     }
//     stages {
//         stage('Build and Push Image') {
//             steps {
//                 script {
//                     // Dockerfile을 사용하여 이미지를 빌드하고 Docker Hub에 푸시
//                     container('kaniko') {
//                         sh """
//                             cp /secret/.dockerconfigjson /kaniko/.docker/config.json
//                         """
//                         sh """
//                             /kaniko/executor --context=${WORKSPACE} --dockerfile=${WORKSPACE}/Dockerfile --destination=dodo133/tws-ai:latest
//                         """
//                     }
//                 }
//             }
//         }
//     }
// }

pipeline {
    agent {
        kubernetes {
            // Kaniko executor 이미지를 사용하여 파드 템플릿을 정의합니다.
            cloud "kubernetes-docker-job"
            yaml '''
                apiVersion: v1
                kind: Pod
                metadata:
                  labels:
                    role: kaniko
                spec:
                  containers:
                  - name: kaniko
                    image: gcr.io/kaniko-project/executor:debug
                    command:
                    - /busybox/cat
                    imagePullPolicy: Always
                    tty: true
                '''
        }
    }
    environment {
        DOCKERHUB_USERNAME = 'dodo133' // Docker Hub의 사용자 이름을 여기에 넣으세요.
        IMAGE_NAME = 'tws-ai' // 원하는 이미지 이름을 여기에 넣으세요.
    }
    stages {
        stage('Build and Push') {
            steps {
                container('kaniko') {
                    script {
//                         def imageFullName = "${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${gitCommit}"
                        sh """
                        echo 'un: $DOCKERHUB_USERNAME'
                        """
//                         sh """
//                         /kaniko/executor \\
//                             --context ${WORKSPACE} \\
//                             --dockerfile ${WORKSPACE}/Dockerfile \\
//                             --destination ${imageFullName}
//                         """
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
