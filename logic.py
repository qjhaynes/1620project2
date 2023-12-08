from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class that defines what happens when the graphical user interface is interacted with.
    """
    MIN_VOLUME = 0  # Minimum volume constant.
    MAX_VOLUME = 2  # Maximum volume constant.
    MIN_CHANNEL = 0  # Minimum channel constant.
    MAX_CHANNEL = 3  # Maximum channel constant

    def __init__(self) -> None:
        """
        Method to initialize the Logic class.
        """
        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_channel_up.clicked.connect(lambda: self.channel_up())
        self.button_channel_down.clicked.connect(lambda: self.channel_down())
        self.button_volume_up.clicked.connect(lambda: self.volume_up())
        self.button_volume_down.clicked.connect(lambda: self.volume_down())

    def power(self) -> None:
        """
        Method to modify the status of the television power.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to modify the mute when the television is on.
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.label_volume.setText('0')
            else:
                self.label_volume.setText(f'{self.__volume}')

    def channel_up(self) -> None:
        """
        Method to increase the channel when the television is on.
        """
        if self.__status:
            if self.__channel == Logic.MAX_CHANNEL:
                self.__channel = Logic.MIN_CHANNEL
            else:
                self.__channel += 1
            self.label_channel.setText(f'{self.__channel}')

    def channel_down(self) -> None:
        """
                Method to decrease the channel when the television is on.
        """
        if self.__status:
            if self.__channel == Logic.MIN_CHANNEL:
                self.__channel = Logic.MAX_CHANNEL

            else:
                self.__channel -= 1
            self.label_channel.setText(f'{self.__channel}')

    def volume_up(self) -> None:
        """
                Method to increase the volume and modify mute when the television is on.
        """
        if self.__status and self.__volume < Logic.MAX_VOLUME:
            self.__muted = False
            self.__volume += 1
            self.label_volume.setText(f'{self.__volume}')

    def volume_down(self) -> None:
        """
                Method to decrease the volume and modify mute when the television is on.
        """
        if self.__status and self.__volume > Logic.MIN_VOLUME:
            self.__muted = False
            self.__volume -= 1
            self.label_volume.setText(f'{self.__volume}')
