resource  "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_s3_bucket" "upload-data" {
  bucket = "release-service-data-catcher101"

}