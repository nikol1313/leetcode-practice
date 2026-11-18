import { expect, test } from 'vitest';
import { __METHOD__ } from './solution.js';

// Replace with the problem's examples: [args array, expected]
test.each([[[[1, 2, 3]], 0]])('__METHOD__(%j) -> %j', (args, expected) => {
  expect(__METHOD__(...args)).toEqual(expected);
});
