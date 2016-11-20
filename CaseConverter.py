import re
import sublime
import sublime_plugin


class converter1(sublime_plugin.TextCommand):
	def run(self, edit):
		# sublime.views()
		data = 'SHMPT_NO_EXT'
		dataLower = data.lower()

		regex = re.compile('(_[a-z])')

		print(regex.findall(dataLower))
		result = re.sub('(_[a-z])', replaceUpper, dataLower)
		self.view.insert(edit, 0, result)

	def replaceUpper(match):
		return match.group(0).upper().replace('_', '')


