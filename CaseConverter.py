import re
import sublime, sublime_plugin

try:
  import commands
except ImportError:
  pass

class converter1(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				data = self.view.substr(region)
				print(data)
				dataLower = data.lower()

				regex = re.compile('(_[a-z0-9])')
				result = re.sub('(_[a-z0-9])', self.replaceUpper, dataLower)
				self.view.replace(edit, region, result)

	def replaceUpper(self, match):
		return match.group(0).upper().replace('_', '')
