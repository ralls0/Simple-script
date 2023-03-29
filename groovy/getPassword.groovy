import jenkins.*
import jenkins.model.* 
import hudson.*
import hudson.model.*

def getPassword = { idCreds ->
  def jenkinsCredentials = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
          com.cloudbees.plugins.credentials.Credentials.class,
          Jenkins.instance,
          null,
          null
  );
  for (creds in jenkinsCredentials) {
    if (idCreds == creds.id) {
      return creds.secret
    }
  }
}
