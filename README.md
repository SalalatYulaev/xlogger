# Import module
from xlogger import XLogger


# Use module in your project
logdir = "my_logs" # default = "logs"
debugger = True # write debug logs to logfile
terminal_debugger = True # print debug logs to stdout
logtype = 'type1' # type1 format: "%Y-%m-%d".log type2 format: "%Y-%m-%d_%H-%M-%S".log
disable_warnings = False # print/not print warnings to stdout
debug_level = 0 # Not yet implemented


log = XLogger (
	logdir = logdir,
	debugger = debugger,
	terminal_debugger = terminal_debugger,
	logtype = "type1",
	disable_warnings = disable_warnings,
	# debug_level = 0,
	)


# After creating 'log' object you can re-define logdir by calling 'subfolder' method:
log.subfolder("another_log_dir")


# If is suitable for applications that use different logdirs for different services. You can create parent class Config, define 'log' object and the re-define logfile for another child class like this:
class Config:
	def __init__(self):
		self.log = XLogger(
		logdir = "main_logs_dir",
		debugger = debugger,
		terminal_debugger = terminal_debugger,
		logtype = "type1",
		disable_warnings = disable_warnings,
		)
		
class MyApp (Config):
	def __init__(self, *args, **kwargs):
		super().__init__()
		self.log.subfolder("application_logs_dir")
		
	
# Call 'log' object to log messages of your application
log.info("This is INFO message")
log.info(f"This is info message with {your_variable}")
log.warning("This is WARNING message")
log.error("This is ERROR message")
log.debug("This is DEBUG message")


# If debugger == False, only 'INFO' and 'ERROR' messages are shown.

