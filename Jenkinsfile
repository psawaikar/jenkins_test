node {
    def app1

    stage('Checkout') {
        checkout scm
    }

    stage('Dev') {
        //echo "Hello World"
        app1 = docker.build('psawaikar/testjenkins:2.0')

        //**** Unit Testing of each docker image goes here -- ADD LATER

        //docker.image('alpine:latest').inside {
        //sh 'echo Hello World!'
        //}
    }

    stage('BAT') {
        //**** BAT tests to be run here -- ADD LATER
        //app1.push()

        docker.withRegistry('https://www.docker.com/', 'psawaikar-DockerHub') {

            app1.push()
        }
    }

    stage('QA') {
        //**** QA tests to be run here -- ADD LATER
        echo "QA Stage - TBD LATER"
    }





}