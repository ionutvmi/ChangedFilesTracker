# changed files tracker sublime plugin
# Author Mihai Ionut Vilcu (ionutvmi@gmail.com)
# Aug 2013

import sublime, sublime_plugin, os, shutil


class ChangedFileTracker(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings("changedFilesTracker.sublime-settings")
		paths = settings.get("paths")
		for path in paths:
			self.checkFiles(path, view)

	def checkFiles(self, path, view):
		file_name = view.file_name()
		# check if the path is in the file name
		if path in file_name: 

			# we build the path to the changed file from the wach folder inside _changed dir
			# if file was in inc/set.php we build _changed/inc
			relPath = file_name.replace(path, "")
			file_dir = path + "/_changed"+ os.path.dirname(relPath)
			if not os.path.exists(file_dir):
				os.makedirs(file_dir)
			
			# we now copy the file that was saved to _changed folder
			shutil.copy(file_name, file_dir + "/" + os.path.basename(relPath))

