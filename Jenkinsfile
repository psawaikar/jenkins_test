node {
    def app1

    stage('Checkout') {
        checkout scm

        def gitTag = gitTagName()
        sh "echo ${gitTag} "

 


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
    // ${workspace} will still contain an absolute path to job workspace on slave

        // When using a GString at least later Jenkins versions could only handle the env.WORKSPACE variant:
        echo "Current workspace is ${env.WORKSPACE}"

       // withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-parag', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
       //  sh "aws s3 ls"
       //  sh "aws s3 cp ${workspace} s3://ambuilds/testbuild --recursive"
       //  }
    }

    stage('QA') {
        //**** QA tests to be run here -- ADD LATER
        echo "QA Stage - TBD LATER"
    }

}
/** @return The tag name, or `null` if the current commit isn't a tag. */
String gitTagName() {
    commit = getCommit()
    if (commit) {
        desc = sh(script: "git describe --tags ${commit}", returnStdout: true)?.trim()
        if (isTag(desc)) {
            return desc
        }
    }
    return null
}

/** @return The tag message, or `null` if the current commit isn't a tag. */
String gitTagMessage() {
    name = gitTagName()
    msg = sh(script: "git tag -n10000 -l ${name}", returnStdout: true)?.trim()
    if (msg) {
        return msg.substring(name.size()+1, msg.size())
    }
    return null
}

String getCommit() {
    return sh(script: 'git rev-parse HEAD', returnStdout: true)?.trim()
}

@NonCPS
boolean isTag(String desc) {
    match = desc =~ /.+-[0-9]+-g[0-9A-Fa-f]{6,}$/
    result = !match
    match = null // prevent serialisation
    return result
}


