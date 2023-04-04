import com.cloudbees.plugins.credentials.Credentials
import org.jenkinsci.plugins.plaincredentials.impl.FileCredentialsImpl

import jenkins.model.*
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey
import org.jenkinsci.plugins.plaincredentials.StringCredentials
import org.jenkinsci.plugins.plaincredentials.impl.FileCredentialsImpl






Set<Credentials> allCredentials = new HashSet<Credentials>();

def creds = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
     com.cloudbees.plugins.credentials.Credentials.class
);
println("GLOBAL CREDENTIAL :")
for (c in creds) {
   
   println("CRED ID = "+c.id + " : ")
  if (c.properties.username) {
    println("   description: " + c.description)
  }
  if (c.properties.username) {
    println("   username: " + c.username)
  }
  if (c.properties.password) {
    println("   password: " + c.password)
  }
  if (c.properties.passphrase) {
    println("   passphrase: " + c.passphrase)
  }
  if (c.properties.secret) {
    println("   secret: " + c.secret)
  }
  if (c.properties.privateKeySource) {
    println("   privateKey: " + c.getPrivateKey())
  }
  println("")
}



Jenkins.instance.getAllItems(com.cloudbees.hudson.plugins.folder.Folder.class).each{ f ->
creds = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
      com.cloudbees.plugins.credentials.Credentials.class, f)
  println("--------------")
  println("CREDENTIAL STORED IN : "+f)
  for (c in creds) {
   
   println("CRED ID = "+c.id + " : ")
  if (c.properties.username) {
    println("   description: " + c.description)
  }
  if (c.properties.username) {
    println("   username: " + c.username)
  }
  if (c.properties.password) {
    println("   password: " + c.password)
  }
  if (c.properties.passphrase) {
    println("   passphrase: " + c.passphrase)
  }
  if (c.properties.secret) {
    println("   secret: " + c.secret)
  }
  if (c.properties.privateKeySource) {
    println("   privateKey: " + c.getPrivateKey())
  }
  if (c.properties.content?.text) {
    println("   secret file : " + c.content?.text)
  } 
  println("")
}
  
}
