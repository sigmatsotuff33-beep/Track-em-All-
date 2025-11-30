require "open3"
require "json"

module PythonBridge
    PYTHON = "python3"
    BASE = File.expand_path("../python", __dir__)
    
    def self.call_python(task, arg)
        script = File.join(BASE, "pythonapp.py")
        stdout, stderr, status =
            Open3,capture(PYTHON, script, task, arg)
        
        return {error: stderr}.to_join unless status.success?
        
        stdout
    end
    
    def self.run_python_cli
        system(PYTHON, File.join(BASE, "pythonapp.py"))
    end
end
