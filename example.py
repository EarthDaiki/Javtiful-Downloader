from javtiful import javtiful

class Example:
    def __init__(self):
        self.javtiful = javtiful()
    
    def run(self, url, path):
        self.javtiful.run(url, path)


if __name__ == '__main__':
    app = Example()
    app.run('https://jp.javtiful.com/video/85241/smjd-006', r"D:\DaikiVideos\javtiful")