@Library('tws-ci-library') _
pipeline {
    agent {
        kubernetes {
//             cloud "kubernetes-docker-job"
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
        GIT_COMMIT_SHORT = sh(script: 'echo $GIT_COMMIT | cut -c 1-7', returnStdout: true).trim()
        MANIFEST_REPO = 'https://github.com/Trans-World-Style/Trans-World-Style-Infra.git'  // 매니페스트 저장소의 URL을 여기에 입력
        MANIFEST_DIR = 'k8s/product/ai'  // 매니페스트 저장소를 체크아웃할 디렉토리
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
//                         buildAndPush(DOCKERHUB_USERNAME, IMAGE_NAME, env.DOCKER_TAG)
                        sh "ls /kaniko/.docker"

                        sh """
                        echo '${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.DOCKER_TAG}'
                        """
                    }
                }
            }
        }
    }
    stage('Update Manifests and Push to Git') {
        steps {
            script {
                // 매니페스트 저장소 체크아웃
                sh "git clone ${MANIFEST_REPO} ${MANIFEST_DIR}"

                // 매니페스트에서 이미지 태그 업데이트
                sh """
                sed -i 's|${DOCKERHUB_USERNAME}/${IMAGE_NAME}:.*|${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.DOCKER_TAG}|' ${MANIFEST_DIR}/ai-deploy-gpu.yaml
                """

                // 변경된 매니페스트를 Git에 푸시
                dir(MANIFEST_DIR) {
                    sh """
                    git config user.name "DW-K"
                    git config user.email "pch145@naver.com"
                    git add .
                    git commit -m "Update image tag to ${env.DOCKER_TAG}"
                    git push origin main
                    """
                }
            }
        }
    }
}
