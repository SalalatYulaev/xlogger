import os
from datetime import datetime



class XLogger():
	def __init__(self, *args, **kwargs):
		self.__init_parameters(*args, **kwargs)
		# self.__check_logdir(self.logdir)

	def __init_parameters(self, *args, **kwargs):
		if 'logdir' in kwargs.keys():
			self.logdir = kwargs['logdir']
		else:
			self.logdir = "logs"
		# self.__check_logdir(self.logdir)
			
		if 'logtype' in kwargs.keys():
			if kwargs['logtype'] == "type1":
				timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d")
			if kwargs['logtype'] == "type2":
				timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")
			self.logfilename = f"{timestamp}.log"
		else:
			timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d")
			self.logfilename = f"{timestamp}.log"

		self.logfile = f"{self.logdir}/{self.logfilename}"

		if 'debugger' in kwargs.keys():
			self.debugger = kwargs['debugger']
		else:
			self.debugger = False

		if 'terminal_debugger' in kwargs.keys():
			self.terminal_debugger = kwargs['terminal_debugger']
		else:
			self.terminal_debugger = False

		if 'debug_level' in kwargs.keys():
			self.debug_level = kwargs['debug_level']
		else:
			self.debug_level = False

		if 'disable_warnings' in kwargs.keys():
			self.disable_warnings = kwargs['disable_warnings']
		else:
			self.disable_warnings = False

	def __check_logdir(self, path):
		if not os.path.exists(path):
			os.makedirs(path)
			return path


	@staticmethod
	def log_msg(logfile, flag, data, _print=False):
		self.__check_logdir(self.logdir)
		timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
		with open(logfile, 'a') as f:
			f.write("{:22}{:8}{}\n".format(timestamp, flag, data))
		if _print:
			print("{:22}{:8}{}".format(timestamp, flag, data))

	def info(self, data):
		self.__check_logdir(self.logdir)
		timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
		flag = "INFO"
		self.__log_write(timestamp, flag, data)
		self.__log_print(timestamp, flag, data)

	def error(self, data):
		self.__check_logdir(self.logdir)
		timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
		flag = "ERR"
		self.__log_write(timestamp, flag, data)
		self.__log_print(timestamp, flag, data)

	def warning(self, data):
		self.__check_logdir(self.logdir)
		timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
		flag = "WARN"
		self.__log_write(timestamp, flag, data)
		if self.disable_warnings == False:
			self.__log_print(timestamp, flag, data)

	def debug(self, data):
		self.__check_logdir(self.logdir)
		level = self.debug_level
		if self.debugger:
			timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
			flag = "DEBUG"
			if self.terminal_debugger:
				self.__log_print(timestamp, flag, data)
				self.__log_write(timestamp, flag, data)
			else:
				self.__log_write(timestamp, flag, data)

	def subfolder(self, path):
		self.logdir = f"{self.logdir}/{path}"
		self.logfile = f"{self.logdir}/{self.logfilename}"


	def __log_write(self, timestamp, flag, data):
		with open(self.logfile, 'a') as f:
			f.write("{:22}{:8}{}\n".format(timestamp, flag, str(data)))

	def __log_print(self, timestamp, flag, data):
		print("{:22}{:8}{}".format(timestamp, flag, str(data)))
