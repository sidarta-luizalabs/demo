node {
    stage " 0 | Clone Repo "
        git url: 'https://github.com/sidarta-luizalabs/demo'
        sh "git rev-parse --short HEAD > commit-id"

    stage " 1 | Build w/ Docker plugin"
        id = readFile('commit-id')replace("\n", "").replace("\r", "")
        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
            def img = docker.build("correiabrux/demo:${id}")
            img.push()
        }
    
    stage " 2 | Testing image"
        sh "echo docker run -d -p 8090:8080 --name demo correiabrux/demo:${id}"
        sh "echo curl -v http://localhost:8090/"
        sh "echo docker rm demo --force"
    
    stage " 3 | Deployment"
        sh "kubectl get deployment demo -o yaml | sed 's%correiabrux/demo.*%correiabrux/demo:${id}%' > /tmp/demo.yaml"
        sh "kubectl apply -f /tmp/demo.yaml"
        sh "kubectl rollout status deployment/demo"
}
