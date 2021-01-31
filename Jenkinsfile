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

        docker.withRegistry('https://registry.hub.docker.com/', 'psawaikar-DockerHub') {

            app1.push('2.0')
        }

        def workspace = WORKSPACE
        // ${workspace} will now contain an absolute path to job workspace on slave

        workspace = env.WORKSPACE

         echo "Current workspace is ${env.WORKSPACE}"

         withAWS(region:'us-east-2',credentials:'parag') {

                 def identity=awsIdentity();//Log AWS credentials

                // Upload files from working directory 'dist' in your project workspace
                s3Upload(bucket:"ambuilds/testbuild", workingDir:workspace, includePathPattern:'**/*');
            }

    }

    stage('QA') {
        //**** QA tests to be run here -- ADD LATER
        echo "QA Stage - TBD LATER"
    }





}