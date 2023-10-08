import random

class Song:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.title = None
        self.status = True
        self.played = 0
    
    def getSize(self):
        if self.head:
            temp = self.head
            size = 1
            while(temp.next != self.head):
                size += 1
                temp = temp.next
            return size
        else:
            return 0
    
    def addSong(self,data):
        newSong = Song(data)
        if self.head is None:
            newSong.next = newSong
            newSong.prev = newSong
            self.head = newSong
            self.tail = newSong
            return
        newSong.next = self.head
        newSong.prev = self.tail
        self.tail.next = newSong
        self.head.prev = newSong
        self.tail = newSong
    
    def deleteFirst(self):
        if self.head is self.tail:
            self.head.prev = None
            self.tail.next = None
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        return temp
    
    def deleteLast(self):
        if self.head is self.tail:
            self.head.prev = None
            self.tail.next = None
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        return temp
    
    def deleteIndex(self, index):
        if index < 0:
            print("Index tidak boleh kurang dari 0")
            return
        
        if self.head:
            if index == 0:
                self.deleteFirst()
            elif index == self.getSize() - 1:
                self.deleteLast()
            elif index >= self.getSize() - 1:
                return
            else:
                temp = self.head
                for i in range(0, index):
                    if (temp.next != self.head):
                        temp = temp.next
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
    
    def printSong(self):
        if self.head is None:
            print('Empty')
        if self.head is not None:
            temp = self.head
            i = 0
            while(temp != self.tail):
                print(i+1,'. ',temp.data)
                temp = temp.next
                i = i + 1
            print(i+1,'. ',temp.data)
    
    def getSong(self, index):
        if index < 0:
            print("Index tidak boleh kurang dari 0")
            return
        if self.head:
            if index == 0:
                return self.head.data
            elif index == self.getSize():
                return self.tail.data
                
            else:
                temp = self.head
                for i in range(0, index):
                    if (temp.next != self.head):
                        temp = temp.next
                return temp.data
        return None
            
    def resume(self):
        self.status = True
    
    def pause(self):
        self.status = False

    def CurrentSong(self):
        if self.status:
            print("Now Playing: "+ self.head.data)
        else:
            print('Playlist Is Paused')

    def nextSong(self):
        self.head = self.head.next
        self.played = self.played + 1
        
    def prevSong(self):
        self.head = self.head.prev
        self.played = self.played + 1
    
    def shuffle(self):
        rand = random.randint(1, max(1, self.getSize()-1))
        for i in range(rand):
            self.head = self.head.prev
        self.played = self.played + 1
    
    def cekPlaylist(self):
        temp = self.head
        if temp is None:
            return False
        else:
            return True
    
    def dataOnIndex(self,indeks):
        i = 0
        temp = self.head
        while i != indeks:
            temp = temp.next
            i = i+1
        return temp.data
    
    def checkDouble(self,data):
        if self.head is not None:
            temp = self.head
            while temp != self.tail:
                if temp.data != data:
                    temp = temp.next
                else:
                    return False
            if self.tail.data == data:
                return False
            return True
        else:
            return True
    
    def moveSong(self, indeks):
        pass

class Queue:
    def __init__(self):
        self.top = None
    
    def getSize(self):
        count = 0
        temp = self.top
        while(temp is not None):
            temp = temp.next
            count += 1
        return count
    
    def peek(self):
        return self.top.data
    
    def enqueue (self,data):
        newSong = Song(data)
        if self.top == None:
            self.top = newSong
        else:
            temp = self.top
            while temp.next != None:
                temp = temp.next
            temp.next = newSong
            temp.next.next = None
    
    def dequeue(self):
        if self.top == None:
            print("Kosong")
            return
        temp = self.top
        self.top = self.top.next
        return temp.data
    
    def isEmpty(self):
        if self.top is not None:
            return False
        return True

    def cekQueue(self):
        temp = self.top
        if temp is None:
            return False
        else:
            return True
    
    def showQueue(self):
        temp = self.top
        if temp == None:
            print('Queue Kosong!!') 
        print('List Queue: ')
        i = 0
        while temp != None:
            print(i+1,'. ',temp.data)
            temp = temp.next
            i = i + 1
        
    def removeByIndex(self,index):
        QueueTemp = Queue()
        temp = self.top
        i = 0
        if temp == None:
            print('Queue Kosong')
        else:
            while i != index:
                QueueTemp.enqueue(self.dequeue())
                i = i + 1
            
            self.dequeue()
            
            while self.top != None:
                QueueTemp.enqueue(self.dequeue())
            
            while QueueTemp.top != None:
                self.enqueue(QueueTemp.dequeue())
    
    def playCurrentSong(self):
        temp = self.top
        if temp is None:
            print('Tidak ada lagu yang di Queue')
        else:
            print('Now Playing: ',temp.data)
            
    def nextSong(self):
        next = self.dequeue()
        if next is None:
            print('Tidak ada lagu yang di Queue !!')
        else:
            print('Now Playing: ', next)

class NestedCDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def getSize(self):
        if self.head:
            temp = self.head
            size = 1
            while(temp.next != self.head):
                size += 1
                temp = temp.next
            return size
        else:
            return 0
    
    def addPlaylist(self, data):
        newPlaylist = Song(data)
        if self.head is None:
            newPlaylist.next = newPlaylist
            newPlaylist.prev = newPlaylist
            self.head = newPlaylist
            self.tail = newPlaylist
            return
        newPlaylist.next = self.head
        newPlaylist.prev = self.tail
        self.tail.next = newPlaylist
        self.head.prev = newPlaylist
        self.tail = newPlaylist
    
    def deleteFirst(self):
        if self.head is self.tail:
            self.head.prev = None
            self.tail.next = None
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
    
    def deleteLast(self):
        if self.head is self.tail:
            self.head.prev = None
            self.tail.next = None
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
    
    def removePlaylist(self, index):
        if index < 0:
            print("Index tidak boleh kurang dari 0")
            return
        if self.head:
            if index == 0:
                temp = self.head.data.title
                self.deleteFirst()
                return temp
            elif index == self.getSize() - 1:
                temp = self.tail.data.title
                self.deleteLast()
                return temp
            elif index >= self.getSize() - 1:
                return
            else:
                temp = self.head
                for i in range(0, index):
                    if (temp.next != self.head):
                        temp = temp.next
                temp2 = temp.data.title
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                return temp2
        
    def getPlaylist(self, index):
        if index < 0:
            print("Index tidak boleh kurang dari 0")
            return
        if self.head:
            if index == 0:
                return self.head
            elif index == self.getSize():
                return self.tail
                
            else:
                temp = self.head
                for i in range(0, index):
                    if (temp.next != self.head):
                        temp = temp.next
                return temp
        return None
    
    def currentPlaylist(self):
        return self.head.data

    def nextPlaylist(self):
        self.head = self.head.next
        self.currentPlaylist()        
    
    def prevPlaylist(self):
        self.head = self.head.prev
        self.currentPlaylist()
        
    def printPlaylist(self):
        if self.head is None:
            print('Empty')
        if self.head is not None:
            temp = self.head
            i = 0
            while(temp != self.tail):
                print(i+1,'. ',temp.data.title)
                temp = temp.next
                i = i + 1
            print(i+1,'. ',temp.data.title)
        print()
    
    def showPlayed(self):
        count = 0
        for i in range(self.getSize()):
            if self.getPlaylist(i).data.played == 0:
                count = count + 1
        if count == self.getSize():
            print('Belum ada playlist yang dimainkan')
        else:
            highest = 0
            indeks = 0
            for i in range(self.getSize()):
                if self.getPlaylist(i).data.played > highest:
                    highest = self.getPlaylist(i).data.played
                    indeks = i
            print(self.getPlaylist(indeks).data.title)
    
    def cekFolder(self):
        if self.getSize() == 0:
            return False
        return True
        
# Penampung Playlist
FolderPlaylists = NestedCDLL()
# Queue Music Player
QueueMusic = Queue()

Playlist = CircularDoubleLinkedList()
Playlist2 = CircularDoubleLinkedList()
Playlist.title = 'Indonesia'
Playlist2.title = 'Inggris'
FolderPlaylists.addPlaylist(Playlist)
FolderPlaylists.addPlaylist(Playlist2)

# Playlist Indonesia
Playlist.addSong('Menghapus Jejakmu')
Playlist.addSong('Pelangi')
Playlist.addSong('Do Re Mi')
Playlist.addSong('Tanpamu')
Playlist.addSong('Hatiku')
Playlist.addSong('Permata')
Playlist.addSong('Semata Karenamu')
Playlist.addSong('Kekasih Bayangan')
# Playlist Inggris
Playlist2.addSong('No Way')
Playlist2.addSong('Fight')
Playlist2.addSong('happy Now')
Playlist2.addSong('Clown')
Playlist2.addSong('How Are You')
Playlist2.addSong('Missing You')
Playlist2.addSong("Why can't i be with you")
Playlist2.addSong('Hopeless')

# MENU
while True:
    print('-----------------------------')
    print('MUSIC APP PLAYER')
    print('-----------------------------')
    print('Menu: ')
    print('1. Playlist')
    print('2. Queue ')
    print('3. Mainkan Playlist')
    print('4. Mainkan Queue')
    print('5. Exit')
    print('-----------------------------')
    print('Most Played Playlist: ')
    FolderPlaylists.showPlayed()
    print('-----------------------------')
    pilihan = int(input('Pilih menu: '))
    # Edit Playlist
    if pilihan == 1:
        while True:
            print('-----------------------------')
            print('List Playlist: ')
            FolderPlaylists.printPlaylist()

            print('-----------------------------')
            print('Menu: ')
            print('1. Tambah Playlist')
            print('2. Hapus Playlist')
            print('3. Rename Playlist')
            print('4. Duplikat Playlist')
            print('5. Tambah atau Hapus Lagu Dari Playlist')
            print('6. Show Playlist')
            print('7. Tambahkan ke Queue')
            print('8. Move Song ')
            print('8. Exit')
            print('-----------------------------')
            pilihan2 = int(input(('Pilih Menu: ')))
            if pilihan2 == 1:
                newPlaylist = input('Masukan Judul Playlist: ')
                Playlist = CircularDoubleLinkedList()
                FolderPlaylists.addPlaylist(Playlist)
                Playlist.title = newPlaylist
                print('Playlist ',Playlist.title,'Berhasil ditambahkan!!')
            if pilihan2 == 2:
                print('-----------------------------')
                print('Playlist: ')
                FolderPlaylists.printPlaylist()
                print('-----------------------------')
                removePlaylist = int(input('Playlist Yang Akan Dihapus: '))
                print('Playlist',FolderPlaylists.removePlaylist(removePlaylist-1), 'Berhasil terhapus')
            if pilihan2 == 3:
                print('-----------------------------')
                print('Playlist: ')
                FolderPlaylists.printPlaylist()
                print('-----------------------------')
                renamePlaylist = int(input('Playlist Yang Akan Di Rename: '))
                newTitle = input('Judul Baru: ')
                FolderPlaylists.getPlaylist(renamePlaylist-1).data.title = newTitle
                print('Judul Playlist berhasil diubah')
            if pilihan2 == 4:
                print('-----------------------------')
                print('Playlist: ')
                FolderPlaylists.printPlaylist()
                print('-----------------------------')
                copyPlaylist = int(input('Playlist Yang Akan Di Duplikat: '))
                title = input('Nama Playlist Baru: ')
                temp = CircularDoubleLinkedList()
                temp.data = FolderPlaylists.getPlaylist(copyPlaylist-1).data
                temp.title = title
                for i in range(FolderPlaylists.getPlaylist(copyPlaylist-1).data.getSize()):
                    temp.addSong(FolderPlaylists.getPlaylist(copyPlaylist-1).data.getSong(i))
                FolderPlaylists.addPlaylist(temp)
            if pilihan2 == 5:
                while True:
                    print('-----------------------------')
                    print('Playlist: ')
                    FolderPlaylists.printPlaylist()
                    print('-----------------------------')
                    editPlaylist = int(input('Playlist Yang Akan Di Add / Remove: '))
                    #Menampilkan isi dari Playlist tersebut
                    print('-----------------------------')
                    print(FolderPlaylists.getPlaylist(editPlaylist-1).data.title, "Playlist")
                    print('List Lagu: ')
                    FolderPlaylists.getPlaylist(editPlaylist-1).data.printSong()
                    print('-----------------------------')
                    print('1. Tambahkan Lagu')
                    print('2. Hapus Lagu')
                    print('3. Exit')
                    print('-----------------------------')
                    pilihan3 = int(input(('Pilih Menu: ')))

                    if pilihan3 == 1:
                        songTitle = input('Masukan Lagu Yang Ingin Ditambahkan Ke Dalam Playlist: ')
                        if FolderPlaylists.getPlaylist(editPlaylist-1).data.checkDouble(songTitle) is True:
                            FolderPlaylists.getPlaylist(editPlaylist-1).data.addSong(songTitle)
                            print(songTitle, ' Berhasil Ditambahkan ke dalam Playlist ',FolderPlaylists.getPlaylist(editPlaylist-1).data.title)
                        else:
                            print('Lagu Sudah Ada Di Playlist')
                            print('Apakah masih ingin menambahkan')
                            jawab = str(input('Y/N: '))
                            if jawab == 'Y':
                                FolderPlaylists.getPlaylist(editPlaylist-1).data.addSong(songTitle)
                                print('Lagu ', songTitle,' berhasil ditambahkan')
                            else:
                                print('Tidak ditambahkan')
                    if pilihan3 == 2 :
                        FolderPlaylists.getPlaylist(editPlaylist-1).data.printSong()
                        songRemove = int(input(('Pilih lagu yang akan dihapus: ')))
                        print(FolderPlaylists.getPlaylist(editPlaylist-1).data.dataOnIndex(songRemove-1), ' berhasil di hapus')
                        FolderPlaylists.getPlaylist(editPlaylist-1).data.deleteIndex(songRemove-1)
                    # Exit
                    if pilihan3 == 3:
                        break

            if pilihan2 == 6:
                print('-----------------------------')
                print('Playlist yang tersedia: ')
                FolderPlaylists.printPlaylist()
                print('-----------------------------')
                showPlaylist = int(input('Playlist Yang Akan Di Show: '))
                print('-----------------------------')
                print(FolderPlaylists.getPlaylist(showPlaylist-1).data.title, "Playlist")
                print('List Lagu: ')
                FolderPlaylists.getPlaylist(showPlaylist-1).data.printSong()
                print('-----------------------------')
            
            if pilihan2 == 7:
                print('-----------------------------')
                print('Playlist yang tersedia: ')
                FolderPlaylists.printPlaylist()
                print('-----------------------------')
                chosenPlaylist = int(input('Pilih Playlist: '))
                print('-----------------------------')
                print(FolderPlaylists.getPlaylist(chosenPlaylist-1).data.title, "Playlist")
                print('List Lagu: ')
                FolderPlaylists.getPlaylist(chosenPlaylist-1).data.printSong()
                print('-----------------------------')
                moveToQueue = int(input('Pilih Lagu Yang Akan Dipindahkan Ke Queue: '))
                song = FolderPlaylists.getPlaylist(chosenPlaylist-1).data.dataOnIndex(moveToQueue-1)
                QueueMusic.enqueue(song)
                print(song, ' Berhasil ditambahkan ke Queue')

            if pilihan2 == 8:
                break # Kembali Ke Menu Awal
    # Edit Queue        
    if pilihan == 2:
        while True:
            print('-----------------------------')
            QueueMusic.showQueue()
            print('-----------------------------')
            print('1. Add Song')
            print('2. Remove Song')
            print('3. Exit')
            print('-----------------------------')
            pilihan2 = int(input('Pilih Menu: '))
            
            if pilihan2 == 1:
                judul = input('Masukan judul lagu: ')
                QueueMusic.enqueue(judul)
                print(judul, ' Ditambahkan ke Queue')    
            if pilihan2 == 3:
                break     
            if pilihan2 == 2:
                indeks = int(input('Lagu mana yang ingin diremove: '))
                QueueMusic.removeByIndex(indeks-1)
            
    # Play From Playlist
    if pilihan == 3:
        if FolderPlaylists.cekFolder():
            print('-----------------------------')
            print('1. Mainkan Playlist Secara Keseluruhan')
            print('2. Mainkan Playlist Secara Spesifik')
            print('-----------------------------')
            pilihan2 = int(input('Pilih Menu: '))
            if pilihan2 == 1:
                FolderPlaylists.currentPlaylist().played = FolderPlaylists.currentPlaylist().played + 1
                while True:
                    print('Playlist: ',FolderPlaylists.currentPlaylist().title)
                    FolderPlaylists.currentPlaylist().CurrentSong()
                    print('-----------------------------')
                    print('     "a" --> Mainkan lagu setelahya')
                    print('     "b" --> Mainkan lagu sebelumnya')
                    print('     "c" --> Mainkan lagu secara shuffle / acak')
                    print('     "r" --> Resume / Lanjutkan lagu')
                    print('     "p" --> Pause/ Hentikan lagu')
                    print('     "np" --> Playlist Selanjutnya')
                    print('     "pp" --> Playlist Sebelumnya')
                    print('     "e" --> Kembali ke menu')
                    print('-----------------------------')
                    status = str(input("Masukkan input : "))
                    if (status == 'a'):
                        FolderPlaylists.currentPlaylist().nextSong()
                        print()
                    elif(status == 'b'):
                        FolderPlaylists.currentPlaylist().prevSong()
                        print()
                    elif (status == 'c'):
                        FolderPlaylists.currentPlaylist().shuffle()
                        print()
                    elif(status == 'r'):
                        FolderPlaylists.currentPlaylist().resume()
                    elif(status == 'p'):
                        FolderPlaylists.currentPlaylist().pause()
                    elif(status == 'np'):
                        FolderPlaylists.nextPlaylist()
                    elif(status == 'pp'):
                        FolderPlaylists.prevPlaylist()
                    elif(status == 'e'):
                        break
                    else:
                        print('Invalid Input')
                        print('-----------------------------')
                    

            if pilihan2 == 2:
                FolderPlaylists.printPlaylist()
                print('-----------------------------')
                indeks = int(input('Pilih Playlist Yang Akan Dimainkan: '))
                if FolderPlaylists.getPlaylist(indeks-1).data.cekPlaylist():
                    FolderPlaylists.getPlaylist(indeks-1).data.played = FolderPlaylists.getPlaylist(indeks-1).data.played + 1
                    while True:
                        print('-----------------------------')
                        FolderPlaylists.getPlaylist(indeks-1).data.CurrentSong()
                        print('-----------------------------')
                        print('     "a" --> Mainkan lagu setelahya')
                        print('     "b" --> Mainkan lagu sebelumnya')
                        print('     "c" --> Mainkan lagu secara shuffle / acak')
                        print('     "r" --> Resume / Lanjutkan lagu')
                        print('     "p" --> Pause/ Hentikan lagu')
                        print('     "e" --> Kembali ke menu')
                        print('-----------------------------')
                        status = str(input("Masukkan input : "))
                        if (status == 'a'):
                            FolderPlaylists.getPlaylist(indeks-1).data.prevSong()
                        elif(status == 'b'):
                            FolderPlaylists.getPlaylist(indeks-1).data.nextSong()
                        elif (status == 'c'):
                            FolderPlaylists.getPlaylist(indeks-1).data.shuffle()
                        elif(status == 'e'):
                            break
                        elif(status == 'r'):
                            FolderPlaylists.getPlaylist(indeks-1).data.resume()
                            FolderPlaylists.getPlaylist(indeks-1).data.CurrentSong()
                        elif(status == 'p'):
                            FolderPlaylists.getPlaylist(indeks-1).data.pause()
                            FolderPlaylists.getPlaylist(indeks-1).data.CurrentSong()
                        else:
                            print('Invalid input!')
                            print()
                        print('-----------------------------')
                # Kalau Isi dari Playlist Kosong
                else:
                    print('Tidak ada lagu yang dapat diputar')
                    print('Segera isi playlist anda dengan lagu-lagu favorit anda')
            # Kalau Isi dari Folder Playlist Kosong        
            else:
                print('Tidak ada playlist yang dapat dimainkan')
                print('Segera daftarkan playlist anda!')
            
    # Play From Queue        
    if pilihan == 4:
        if QueueMusic.cekQueue():
            while True:
                print('-----------------------------')
                QueueMusic.showQueue()
                print('-----------------------------')
                QueueMusic.playCurrentSong()
                print('-----------------------------')
                print('     "a" --> Mainkan Lagu Berikutnya')
                print('     "e" --> Kembali ke Menu')
                print('-----------------------------')
                status = str(input("Masukkan input : "))
                print()
                if(status == 'a'):
                    QueueMusic.nextSong()
                    print()
                elif(status == 'e'):
                    break
                else:
                    print('Input Tidak Sesuai!')
                    print()
                print('-----------------------------')
        # Kalau Queue Masih Kosong
        else:
            print('Belum ada lagu yang di Queue!!')
    # Exit
    if pilihan == 5:
        exit()