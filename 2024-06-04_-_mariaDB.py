sudo apt purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-* #1:
sudo apt purge docker-desktop #1:
sudo apt autoremove #1:
sudo apt autoclean #1:
sudo apt update #2:
sudo apt install mariadb-server mariadb-client #3:
sudo systemctl start mariadb #4:
sudo systemctl enable mariadb #4:
sudo systemctl status mariadb #5:
sudo mysql_secure_installation #6:
sudo mysql -u root -p #7:
SHOW DATABASES; #8:
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY '123456' WITH GRANT OPTION; #9:
FLUSH PRIVILEGES; #9:
CREATE DATABASE base_de_dados; #10:
USE base_de_dados; #11:
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'senha_usuario'; #12:
GRANT ALL PRIVILEGES ON base_de_dados.* TO 'usuario'@'localhost'; #13:
FLUSH PRIVILEGES; #14:
SELECT User, Host FROM mysql.user; #15:
sudo systemctl stop mariadb #16:
