<?php

class GraphNode {
    public const TYPE_FRESH = 'fresh';
    public const TYPE_ROTTEN = 'rotten';
    public const BIG_NUMBER = 100;

    private array $neighbours;
    private int $minDistance;
    private string $type;
    private string $key;

    public function __construct(string $key, int $type)
    {
        $this->neighbours = [];
        $this->key = $key;

        switch ($type) {
            case 2:
                $this->minDistance = 0;
                $this->type = self::TYPE_ROTTEN;
                break;
            case 1:
                $this->minDistance = self::BIG_NUMBER;
                $this->type = self::TYPE_FRESH;
                break;
        }
    }
    
    public function addNeighbour(string $node): GraphNode
    {
        $this->neighbours[] = $node;
        return $this;
    }

    public function getNeighbours(): array
    {
        return $this->neighbours;
    }

    public function updateMinDistance(int $distance): void
    {
        if ($distance < $this->minDistance) {
            $this->minDistance = $distance;
        }
    }

    public function getMinDistance(): int
    {
        return $this->minDistance;
    }

    public function getType(): string
    {
        return $this->type;
    }

    public function getKey(): string
    {
        return $this->key;
    }
}

class Solution
{
    private int $numberOfRows;
    private int $numberOfColumns;
    private array $graphNodes;

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    public function orangesRotting(array $grid): int
    {
        $this->numberOfRows = count($grid);
        $this->numberOfColumns = count($grid[0]);

        $this->graphNodes = $this->getGraphNodes($grid);
        $this->updateNeighbors($grid);
        $rottenNodes = $this->getRottenNodes();
        $this->updateMinDistances($rottenNodes);
        return $this->findAnswer();
    }

    private function getKeyOfGraphNode(int $row, int $column): string
    {
        return "$row-$column";
    }

    private function getCoordinatesFromKey(string $key): array
    {
        return explode('-', $key);
    }

    private function getNeighboursCoordinates(string $key, array $grid): array
    {
        $neighbours = [];

        [$row, $column] = $this->getCoordinatesFromKey($key);

        if ($row > 0 && $grid[$row-1][$column] > 0) {
            $neighbours[] = $this->getKeyOfGraphNode($row-1, $column);
        }

        if ($row < $this->numberOfRows - 1 && $grid[$row+1][$column] > 0) {
            $neighbours[] = $this->getKeyOfGraphNode($row+1, $column);
        }

        if ($column > 0 && $grid[$row][$column-1] > 0) {
            $neighbours[] = $this->getKeyOfGraphNode($row, $column-1);
        }

        if ($column < $this->numberOfColumns - 1 && $grid[$row][$column+1] > 0) {
            $neighbours[] = $this->getKeyOfGraphNode($row, $column+1);
        }

        return $neighbours;
    }

    private function getGraphNodes(array $grid): array
    {
        $graphNodes = [];

        for ($row = 0; $row < $this->numberOfRows; $row++) {
            for ($column = 0; $column < $this->numberOfColumns; $column++) {
                $orangeType = $grid[$row][$column];

                if ($orangeType === 0) {
                    continue;
                }

                $key = $this->getKeyOfGraphNode($row, $column);
                $graphNodes[$key] = (new GraphNode($key, $orangeType));
            }
        }
        return $graphNodes;
    }

    private function updateNeighbors(array $grid): void
    {
        foreach ($this->graphNodes as $key => $node) {
            /** @var $node GraphNode */
            foreach ($this->getNeighboursCoordinates($key, $grid) as $neighborKey) {
                $node->addNeighbour($neighborKey);
            }
        }
    }

    private function getRottenNodes(): array
    {
        $rottenNodes = [];
        foreach ($this->graphNodes as $node) {
            /** @var $node GraphNode */
            if ($node->getType() === GraphNode::TYPE_ROTTEN) {
                $rottenNodes[] = $node;
            }
        }

        return $rottenNodes;
    }

    private function updateMinDistances(array $rottenNodes): void
    {
        foreach ($rottenNodes as $rottenNode) {
            $this->applyBFS($rottenNode);
        }
    }

    private function applyBFS(GraphNode $startNode)
    {
        $queue = [$startNode->getKey() => $startNode];
        $visitedNodes = [$startNode->getKey() => $startNode->getKey()];

        while ($queue) {
            $node = array_shift($queue);
            $visitedNodes[$node->getKey()] = $node->getKey();
            $distance = $node->getMinDistance();

            foreach ($node->getNeighbours() as $neighbourKey) {
                /** @var $neighbour GraphNode */
                $neighbour = $this->graphNodes[$neighbourKey];

                if (isset($visitedNodes[$neighbourKey]) && $neighbour->getMinDistance() < $distance + 1) {
                    continue;
                }

                $neighbour->updateMinDistance($distance + 1);
                $queue[$neighbour->getKey()] = $neighbour;
            }
        }
    }

    private function findAnswer(): int
    {
        $maxDistance = 0;

        foreach ($this->graphNodes as $node) {
            /** @var $node GraphNode */
            $nodeDistance = $node->getMinDistance();

            if ($nodeDistance == GraphNode::BIG_NUMBER) {
                return -1;
            }

            if ($nodeDistance > $maxDistance) {
                $maxDistance = $nodeDistance;
            }
        }

        return $maxDistance;
    }
}

$testCases = [
    [
        'input' => [[2,1,1],[1,1,0],[0,1,1]],
        'output' => 4,
    ],
    [
        'input' => [[2,1,1],[0,1,1],[1,0,1]],
        'output' => -1,
    ],
    [
        'input' => [[0,2]],
        'output' => 0,
    ],
];

foreach ($testCases as $test) {
    $input = $test['input'];
    $output = (new Solution())->orangesRotting($input);
    $expectedOutput = $test['output'];
    if ($output == $expectedOutput) {
        echo "TEST WENT OKAY\n";
    } else {
        print_r($input);
        echo $output . ' should have been ' . $expectedOutput;
        break;
    }
}
