// def dockerTag = ''
// pipeline {
//     agent {
//         kubernetes {
//             // Kaniko executor 이미지를 사용하여 파드 템플릿을 정의합니다.
//             cloud "kubernetes-docker-job"
//             yaml '''
//                 apiVersion: v1
//                 kind: Pod
//                 metadata:
//                   labels:
//                     role: kaniko
//                 spec:
//                   containers:
//                   - name: kaniko
//                     image: gcr.io/kaniko-project/executor:debug
//                     command:
//                     - /busybox/cat
//                     imagePullPolicy: Always
//                     tty: true
//                     volumeMounts:
//                     - name: jenkins-docker-cfg
//                       mountPath: /kaniko/.docker
//                   volumes:
//                   - name: jenkins-docker-cfg
//                     projected:
//                       sources:
//                       - secret:
//                           name: dockerhub-secret
//                           items:
//                             - key: .dockerconfigjson
//                               path: config.json
//                 '''
//         }
//     }
//     environment {
//         DOCKERHUB_USERNAME = 'dodo133' // Docker Hub의 사용자 이름을 여기에 넣으세요.
//         IMAGE_NAME = 'tws-ai' // 원하는 이미지 이름을 여기에 넣으세요.
//     }
//     stages {
//         stage('extract docker tag') {
//             steps {
//                 script {
//                     def commitHash = env.GIT_COMMIT
//                     def commitMessage = sh(script: "git log -1 --pretty=%B ${commitHash}", returnStdout: true).trim()
//                     def match = commitMessage =~ /tag: (\S+)/
//                     if(match) {
//                         dockerTag = match[0][1]
//                         echo "Commit Tag: ${dockerTag}"
//                     } else {
//                         error("Tag not found in commit message!\ncommit message: ${commitMessage}")
//                     }
//                 }
//             }
//         }
//         stage('Build and Push') {
//             steps {
//                 container('kaniko') {
//                     script {
//                         def imageFullName = "${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${dockerTag}"
//                         sh """
//                         /kaniko/executor --context `pwd` --verbosity debug --destination ${imageFullName} --cache
//                         """
// //                         sh """
// //                         echo '${imageFullName}'
// //                         """
//                     }
//                 }
//             }
//         }
//     }
// }
@Library('tws-ci-library') _
pipeline {
    agent {
        kubernetes {
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
                    volumeMounts:
                    - name: jenkins-docker-cfg
                      mountPath: /kaniko/.docker
                  volumes:
                  - name: jenkins-docker-cfg
                    projected:
                      sources:
                      - secret:
                          name: dockerhub-secret
                          items:
                            - key: config.json
                              path: config.json
                '''
        }
    }
    environment {
        DOCKERHUB_USERNAME = 'dodo133' // Docker Hub의 사용자 이름을 여기에 넣으세요.
        IMAGE_NAME = 'tws-ai' // 원하는 이미지 이름을 여기에 넣으세요.
    }
    stages {
        stage('extract docker tag') {
            steps {
                script {
                    env.DOCKER_TAG = extractDockerTag()
                }
            }
        }
        stage('Build and Push') {
            steps {
                container('kaniko') {
                    script {
                        buildAndPush(DOCKERHUB_USERNAME, IMAGE_NAME, env.DOCKER_TAG)
                        sh "ls /kaniko/.docker"

                        sh """
                        echo '${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.DOCKER_TAG}'
                        """
                    }
                }
            }
        }
    }
}