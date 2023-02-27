pipeline {
    agent any

        environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = "us-east-1"
        DOCKERHUB_CREDENTIALS = credentials('docker')
    }

    // Cloning Git
    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/vibhor-07/polling.git']]])     
            }
        }

    // Building Docker images
    stage('Building Docker image') {
      steps {
        script {
            dir('application') {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'echo admin | sudo docker build -t vibhor07/polling .'
            }
        }
      }
    }
   
    
    // Push Image to Docker Hub
    stage('Push Image to Docker Hub') {         
        steps {           
        sh 'sudo docker push vibhor07/polling'           
        echo 'Push Image Completed'       
    }            
}
    // Create an EKS Cluster
    stage("Create an EKS Cluster") {
            steps {
                script {
                    dir('terraform') {
                        sh "terraform init"
                        sh "terraform apply -auto-approve"
                    }
                }
            }
        }

    // Deploy to EKS
     stage("Deploy to EKS") {
            steps {
                script {
                    dir('application') {
                        sh "pwd"
                        sh "aws eks update-kubeconfig --name myapp-eks-cluster"
                        sh "kubectl delete -f Deployment.yml"
                        sh "kubectl apply -f Deployment.yml"
                        sh "cat Deployment.yml"
                        sh "kubectl get svc"
                    }
                }
            }
        }
    }
}