Change current directory to initial/src where there is file run.py
Type: python3 run.py gen 
Then type: python3 run.py test LexerSuite
Then type: python3 run.py test ParserSuite



cd src

cd usr/src/PPL

apt-get update
apt-get install -y python3 python3-pip
apt-get install -y default-jre default-jdk

python3 --version
java --version

export ANTLR_JAR="/usr/src/PPL/antlr-4.9.2-complete.jar"
echo $ANTLR_JAR

apt install -y python3.12-venv


python3 -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt
