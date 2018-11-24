from telethon.tl import TLObject


class ChannelParticipantsAdmins(TLObject):
    CONSTRUCTOR_ID = 0xb4608969
    SUBCLASS_OF_ID = 0xbf4e2753

    def to_dict(self):
        return {
            '_': 'ChannelParticipantsAdmins'
        }

    def __bytes__(self):
        return b''.join((
            b'i\x89`\xb4',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()