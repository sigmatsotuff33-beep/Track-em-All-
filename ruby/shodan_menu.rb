require_relative "python_bridge"

module ShodanMenu
  def self.prompt
    print "IP: "
    ip = gets.chomp

    print "Shodan API key: "
    api = gets.chomp

    
    args = "#{ip}|#{api}"
    result = PythonBridge.call_python("shodan", args)

    puts result
  end
end
