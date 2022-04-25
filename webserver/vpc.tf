
resource "aws_vpc" "bibbo-vpc" {
  cidr_block = "10.1.0.0/16"
}

resource "aws_subnet" "public-subnet" {
    vpc_id     = aws_vpc.bibbo-vpc.id
    cidr_block = "10.1.1.0/24"
    availability_zone = "us-west-2a"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.bibbo-vpc.id
}

resource "aws_route_table" "routetable" {
  vpc_id = aws_vpc.bibbo-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
} 

resource "aws_route_table_association" "routetable-association" {
  route_table_id = aws_route_table.routetable.id
  subnet_id = aws_subnet.public-subnet.id
} 

resource "aws_security_group" "allow_http" {
  name        = "allow_http"
  description = "Allow http traffic"
  vpc_id      = aws_vpc.bibbo-vpc.id
  ingress {
    description = "Http"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "ssh"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_instance" "bibbo-webserver" {
  ami                         = "ami-02b92c281a4d3dc79"
  instance_type               = "t2.micro"
  availability_zone           = "us-west-2a"
  subnet_id                   = aws_subnet.public-subnet.id
  associate_public_ip_address = true
  key_name                    = aws_key_pair.ssh.key_name
  security_groups             = [aws_security_group.allow_http.id]
  iam_instance_profile        = "LabInstanceProfile"
  user_data                   = "${file("modules/tf-user-data.sh")}"
   tags                      = {
        Name = "bibbo-webserver"
        }
}
resource "aws_eip" "bibbo-webserver" {
  instance = aws_instance.bibbo-webserver.id
  vpc      = true
}
