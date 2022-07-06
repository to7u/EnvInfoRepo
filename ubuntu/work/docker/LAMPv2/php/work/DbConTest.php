<?php
/**
 * environment:
 * MYSQL_ROOT_PASSWORD=root
 * MYSQL_DATABASE=test
 * MYSQL_USER=test
 * MYSQL_PASSWORD=test
 */

try {
    // host=XXXの部分のXXXにはmysqlのサービス名を指定
    $dsn = 'mysql:host=db;dbname=test;';
b = new PDO($d,'test', 'test');

    $sql SELECT version();';
    $dsn = '    $stmt = $db->prepare($sql);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    echo("conection ok \n");
    var_dump($result);
} catch (PDOException $e) {
    echo $e->getMessage();
    exit;
}

?>
