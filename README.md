# netspyre
Automated GUI-Based Multi-Tool for Penetration Testing

NetSpyre (https://github.com/vikram249/netspyre)
==

Authors:
----
Asia Pacific University 

  Vikram Prasad (vikramprasad249@gmail.com)


Description
----

NetSpyre is Python-based GUI application basically designed to streamline penetration testing or vulnerability assessment, particularly during the scanning and enumeration phases while packing a bruteforce tool as an additional feature to it from discovering the services attached to it. It empowers penetration testers and cybersecurity enthusiasts by providing a user-friendly interface that simplifies access to their toolkit and presents all of the tool outputs in a user-friendly format. By minimizing the setup time for the commands and tools, NetSpyre maximizes the time available for then result analysis. However one of the most eye-catching feature is the fact that NetSpyre offers its users to customize options for commands and tools. 



Requirements
----

It is recommended to use Kali Linux as it comes with most of the required tools pre-installed. However, NetSpyre is likely to function effectively on most of the Linux-based distributions out there as well.

Kali 2023:

    sudo apt install python3-sqlalchemy python3-pyqt5 wkhtmltopdf


Apart from these, the following tools are required for NetSpyre to have its minimum functionality:
- nmap (for adding hosts to the scope)
- hydra (for the brute tab)

In Kali Linux, to ensure that all of the tools used by NetSpyre's default configuration use:

    apt-get install ldap-utils rwho rsh-client x11-apps finger

Installation
----

    cd /usr/share/
    git clone https://github.com/vikram249/netspyre.git

    Place the "netspyre" file in /usr/bin/ and make it executable.
    Type 'sudo netspyre' in any terminal to launch the application.


Credits
----

I extend my heartfelt gratitude to my supervisor, Ms. Nurul Haniza Mohtar, and my seocnd marker, Ms. Nor Azlina Abdul Rahman. Their unwavering support and valuable ideas were instrumental and important throughout the development of the NetSpyre application. Their guidance and mentorship have been invaluable in shaping this whole project. 

I would like thank extend my greatefulness towards Asia Pacific University for providing me with the opportunity to showcase this project, allowing me to share my efforts and learning journey. 
