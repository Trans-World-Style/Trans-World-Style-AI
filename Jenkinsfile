pipeline {
    agent any // 혹은 다른 agent 지정
    triggers {
        githubPush()
    }
    stages {
        stage('Setup and Deploy') {
            when {
                anyOf {
                    branch 'main'
                    branch 'test'
                }
            }
            steps {
                script {
                    sh """
                        echo 'test run!!!!'
                    """
                }
            }
        }
    }
}
