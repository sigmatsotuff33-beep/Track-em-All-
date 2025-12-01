require "open3"

module PythonBridge
  PYTHON = "python3"     
  SCRIPT  = "../pythonapp.py"  

  def self.call_python(task, arg)
    stdout, stderr, status = Open3.capture3(PYTHON, SCRIPT, task, arg)

    if status.success?
      stdout
    else
      "Python error: #{stderr}"
    end
  end

  def self.run_python_cli
    system(PYTHON, SCRIPT)
  end
end
