import deeplabcut


# deeplabcut.create_new_project(‘Name of the project’,‘Name of the
# experimenter’, [‘Full path of video 1’,‘Full path of video2’, . . .],working_directory=‘Full path of the working directory’,copy_videos=
# True/False)

# path_config_file = deeplabcut.create_new_project('fruitflyMotionTracker_test1','temp', ['C:\\Users\\Ben Gao\\Documents\\GitHub\\Fruitfly\\test1.avi'],working_directory='C:\\Users\\Ben Gao\\Documents\\GitHub\\Fruitfly',copy_videos=True)
path_config_file = 'C:\\Users\\Ben Gao\\Documents\\GitHub\\Fruitfly\\fruitflyMotionTracker_test1-temp-2021-10-07\\config.yaml'


path_config_file


deeplabcut.extract_frames(path_config_file'automatic','uniform', userfeedback = True)


get_ipython().run_line_magic("gui", " wx")
deeplabcut.label_frames(path_config_file)


deeplabcut.check_labels(path_config_file)


deeplabcut.create_training_dataset(path_config_file, num_shuffles=1)


# 之前直接拿CPU跑了两天一夜，不知道这个loss要多接近0才算训练完成。

deeplabcut.train_network(path_config_file)



