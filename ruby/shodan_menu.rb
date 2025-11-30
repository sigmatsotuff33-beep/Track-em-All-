require_relative "python_bridge"

module ShodanMenu
    def self.prompt
        print "IP: "
        ip = gets.chomp
        print "Shodan API key: "
        api = gets.chomp
        
        result = PythonBridge.call_python("shodan, "#{ip}|api}")
            puts result
            end
    end
    
    