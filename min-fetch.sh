. /etc/os-release
DISTRO="${PRETTY_NAME:-Linux}"
KERNEL=$(uname -r)
SHELL="${SHELL##*/}"
UPTIME=$(uptime -p)
UPTIME=${UPTIME:3}

echo "distro: $DISTRO" | awk '{print tolower($0)}'
echo "kernel: $KERNEL" | awk '{print tolower($0)}'
echo "shell: $SHELL" | awk '{print tolower($0)}'
echo "uptime: $UPTIME" | awk '{print tolower($0)}'
