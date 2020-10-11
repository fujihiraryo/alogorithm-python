# python-kyopro-library

競プロ用 Python ライブラリ

## 幾何

| コード                       | 説明         |
| :--------------------------- | :----------- |
| [geometry/circle.py](geometry/circle.py) | 円   |
| [geometry/convex.py](geometry/convex.py) | 凸包   |
| [geometry/distance.py](geometry/distance.py) | 点と線分の距離 |
| [geometry/intersect.py](geometry/intersect.py) | 線分の交差判定 |
| [geometry/triangle.py](geometry/triangle.py) | 三角形   |

## グラフ

| コード                       | 説明         |
| :--------------------------- | :----------- |
| [graph/bellman_ford.py](graph/bellman_ford.py) | ベルマンフォード法  |
| [graph/bfs.py](graph/bfs.py) | 幅優先探索   |
| [graph/dfs.py](graph/dfs.py) | 深さ優先探索 |
| [graph/dijkstra.py](graph/dijkstra.py) | ダイクストラ法  |
| [graph/grid.py](graph/grid.py) |グリッドを隣接リストに変換 |
| [graph/topological_sort.py](graph/topological_sort.py) | トポロジカルソート |
| [graph/warshall_floyd.py](graph/warshall_floyd.py) | ワーシャルフロイド法 |

## 整数

| コード                                       | 説明                     |
| :------------------------------------------ | :---------------------- |
| [integer/comb.py](integer/comb.py) | 二項係数 |
| [integer/discrete_log.py](integer/discrete_log.py) | 離散対数 |
| [integer/euclid.py](integer/euclid.py)| ユークリッドの互除法 |
| [integer/factrization.py](integer/factrization.py) | 素因数分解 |
| [integer/fft.py](integer/fft.py) | 剰余環上の高速フーリエ変換 |
| [integer/lagrange.py](integer/lagrange.py) | 剰余環上の多項式のラグランジュ補間 |
| [integer/mint.py](integer/mint.py) | 自動でmodをとる整数型 |
| [integer/polynomial.py](integer/polynomial.py) | 剰余環上の多項式の積分 |

## 探索

| コード                       | 説明   |
| :--------------------------- | :----- |
| [search/bisect.py](search/bisect.py)   | 二分探索  |
| [search/bit.py](search/bit.py) | bit全探索 |
| [search/generator.py](search/generator.py) | ジェネレーター |
| [search/trisect.py](search/trisect.py)   | 三分探索  |

## 文字列

| コード                       | 説明   |
| :--------------------------- | :----- |
| [string/edit_distance.py](string/edit_distance.py)   | 編集距離 |
| [string/lcs.py](string/lcs.py)   | 最長共通部分列 |
| [string/rolling_hash.py](string/rolling_hash.py)   | ローリングハッシュ  |
| [string/z_algorithm.py](string/z_algorithm.py)   | Z-Algorithm  |

## データ構造

| コード                                             | 説明         |
| :------------------------------------------------- | :----------- |
| [structure/segtree.py](structure/segtree.py)       | セグメント木 |
| [structure/rooted_tree.py](structure/rooted_tree.py)   | 根付き木 |
| [structure/union_find.py](structure/union_find.py) | Union Find   |
