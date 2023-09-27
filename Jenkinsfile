// @Library('tws-ci-library') _
// pipeline {
//     agent {
//         kubernetes {
// //             cloud "kubernetes-docker-job"
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
//                             - key: config.json
//                               path: config.json
//                 '''
//         }
//     }
//     environment {
//         DOCKERHUB_USERNAME = 'dodo133' // Docker Hub의 사용자 이름을 여기에 넣으세요.
//         IMAGE_NAME = 'tws-ai' // 원하는 이미지 이름을 여기에 넣으세요.
//         GIT_COMMIT_SHORT = sh(script: 'echo $GIT_COMMIT | cut -c 1-7', returnStdout: true).trim()
//         MANIFEST_REPO = 'Trans-World-Style/Trans-World-Style-Infra.git'  // 매니페스트 저장소의 URL을 여기에 입력
//         MANIFEST_DIR = 'Trans-World-Style-Infra/k8s/product/ai/gpu'
//     }
//     stages {
//         stage('extract docker tag') {
//             steps {
//                 script {
//                     env.DOCKER_TAG = extractDockerTag()
//                 }
//             }
//         }
//         stage('Build and Push') {
//             steps {
//                 container('kaniko') {
//                     script {
// //                         buildAndPush(DOCKERHUB_USERNAME, IMAGE_NAME, env.DOCKER_TAG)
//                         sh "ls /kaniko/.docker"
//
//                         sh """
//                         echo '${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${env.DOCKER_TAG}'
//                         """
//                     }
//                 }
//             }
//         }
//         stage('Update Manifests and Push to Git') {
//             steps {
//                 script {
//                     withCredentials([usernamePassword(credentialsId: 'github-cridentials', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
//                         sh "git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${MANIFEST_REPO}"
//                         sh """
//                         sed -i 's|${DOCKERHUB_USERNAME}/${IMAGE_NAME}:.*|${DOCKERHUB_USERNAME}/${IMAGE_NAME}:test|' ${MANIFEST_DIR}/ai-deploy-gpu.yaml
//                         """
//                         dir(MANIFEST_DIR) {
//                             sh """
//                             git config user.name "DW-K"
//                             git config user.email "pch145@naver.com"
//                             git add .
//                             git commit -m "Update image tag to ${env.DOCKER_TAG}"
//                             git push origin main
//                             """
//                         }
//                     }
//                 }
//             }
//         }
//     }
// }

@Library('tws-ci-library') _

commonPipeline {
    dockerhubUsername = 'dodo133'
    imageName = 'tws-ai'
    manifestRepo = 'Trans-World-Style/Trans-World-Style-Infra.git'
    manifestDir = 'Trans-World-Style-Infra/k8s/product/ai/cpu'
    manifestFile = 'ai-deploy-cpu.yaml'

//     beforeBuildStages = []

    afterBuildStages = [
        'Custom Stage 1': {
            echo "env.DOCKER_TAG"
        },
        'Custom Stage 2': {
            echo "This is custom stage 2"
        }
    ]
}

