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
    environment {
        AWS_ACCESS_KEY = 'AKIA4NJHVZKRCWWUG5KJ'
        AWS_SECRET_KEY = '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'
    }
}

