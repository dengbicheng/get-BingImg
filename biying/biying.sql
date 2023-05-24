
use reptile;
CREATE TABLE biying_images (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增长唯一键',
    img_name VARCHAR(255) COMMENT '图片名称',
    img_link VARCHAR(255) COMMENT '图片链接',
    img_uptime DATETIME COMMENT '图片上传时间',
    downloads INT COMMENT '下载次数'
);

