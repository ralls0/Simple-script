import java.util.concurrent.Callable
import java.util.concurrent.Executors

def sh(cmd) {
    def proc = ["/bin/sh", "-c", cmd].execute()
    def pool = Executors.newFixedThreadPool(2)
    def stdoutFuture = pool.submit({ -> proc.inputStream.text} as Callable<String>)
    def stderrFuture = pool.submit({ -> proc.errorStream.text} as Callable<String>)
    proc.waitFor()
    def exitValue = proc.exitValue()
    if(exitValue != 0) {
        System.err.println(stderrFuture.get())
        throw new RuntimeException("$cmd returned $exitValue")
    }
    return stdoutFuture.get()
}
