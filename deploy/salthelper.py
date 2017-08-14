#coding:utf-8

import salt.client



class SaltHelper:
    def __init__(self):
        self.client = salt.client.LocalClient()

    def alive(self):
        '''
        salt主机存活检测
        '''

        return self.client.cmd_async('*', 'test.fib', [10])

if __name__ == "__main__":
    helper = SaltHelper()
    print helper.alive()