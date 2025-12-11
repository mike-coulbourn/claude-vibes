# Code Generation Slash Command Examples

Real-world commands for generating code, tests, docs, and boilerplate.

## Example 1: Test Generator

**File**: `.claude/commands/gen-tests.md`

```markdown
---
description: Generate comprehensive tests for a file
allowed-tools: Read, Grep, Glob, Write
argument-hint: [file-to-test]
---

## Source Code

@$1

## Existing Test Patterns

@tests/

## Project Testing Guide

@CLAUDE.md

## Test Generation Task

Generate comprehensive tests for @$1:

### Structure

Follow this pattern:
```javascript
describe('[Module/Class name]', () => {
  describe('[function name]', () => {
    it('should [expected behavior]', () => {
      // Arrange: Set up test data
      // Act: Execute function
      // Assert: Verify results
    });
  });
});
```

### Coverage

Create tests for:

**1. Happy Path**
- Normal, expected usage
- Valid inputs
- Expected outputs

**2. Edge Cases**
- Empty inputs
- Null/undefined
- Boundary values
- Maximum values
- Zero values

**3. Error Cases**
- Invalid inputs
- Type mismatches
- Missing parameters
- Exception handling

**4. Integration**
- Dependencies interaction
- External service calls
- Database operations

### Test Organization

```javascript
// Setup
beforeEach(() => {
  // Common setup
});

afterEach(() => {
  // Cleanup
});

// Tests grouped by function
describe('functionName', () => {
  // Happy path first
  it('should work with valid input', () => {});

  // Then edge cases
  it('should handle empty input', () => {});

  // Then errors
  it('should throw on invalid input', () => {});
});
```

### Output

Provide complete test file ready to use.
```

**Usage**:
```
/gen-tests src/utils/validator.js
```

---

## Example 2: API Endpoint Generator

**File**: `.claude/commands/gen-endpoint.md`

```markdown
---
description: Generate REST API endpoint with validation and tests
allowed-tools: Read, Grep, Glob, Write
argument-hint: [endpoint-name] [http-method]
---

## Existing API Patterns

@src/api/users.js
@src/api/posts.js

## Project API Conventions

@CLAUDE.md
@docs/api-design.md

## Generation Task

Create complete API endpoint: $1 (method: $2)

### 1. Route Handler

```javascript
// src/api/$1.js

const express = require('express');
const router = express.Router();

/**
 * $2 $1
 * Description: [What this endpoint does]
 */
router.$2('/$1', async (req, res) => {
  try {
    // Validate input
    // Process request
    // Return response
  } catch (error) {
    // Error handling
  }
});

module.exports = router;
```

### 2. Input Validation

Use validation library:
```javascript
const { body, validationResult } = require('express-validator');

const validateInput = [
  body('field').notEmpty().isString(),
  // More validations
];
```

### 3. Business Logic

Separate logic from route:
```javascript
// src/services/$1.service.js
async function handleRequest(data) {
  // Implementation
}
```

### 4. Tests

```javascript
// tests/api/$1.test.js
describe('$2 $1', () => {
  it('should return 200 with valid input', async () => {});
  it('should return 400 with invalid input', async () => {});
  it('should return 401 without auth', async () => {});
});
```

### 5. Documentation

```markdown
## $2 $1

**URL**: `$1`
**Method**: `$2`
**Auth required**: Yes/No

**Request**:
\```json
{
  "field": "value"
}
\```

**Response**:
\```json
{
  "success": true,
  "data": {}
}
\```
```

Provide all files ready to integrate.
```

**Usage**:
```
/gen-endpoint notifications POST
```

---

## Example 3: React Component Generator

**File**: `.claude/commands/gen-component.md`

```markdown
---
description: Generate React component with tests and stories
allowed-tools: Read, Grep, Glob, Write
argument-hint: [component-name]
---

## Existing Component Examples

@src/components/Button.jsx
@src/components/Card.jsx

## Component Patterns

@CLAUDE.md
@docs/component-guidelines.md

## Generation Task

Create React component: $1

### 1. Component File

```jsx
// src/components/$1.jsx
import React from 'react';
import PropTypes from 'prop-types';
import styles from './$1.module.css';

export const $1 = ({ prop1, prop2, ...props }) => {
  return (
    <div className={styles.container} {...props}>
      {/* Component JSX */}
    </div>
  );
};

$1.propTypes = {
  prop1: PropTypes.string.isRequired,
  prop2: PropTypes.func,
};

$1.defaultProps = {
  prop2: () => {},
};
```

### 2. Styles

```css
/* src/components/$1.module.css */
.container {
  /* Styles */
}
```

### 3. Tests

```jsx
// src/components/$1.test.jsx
import { render, screen } from '@testing-library/react';
import { $1 } from './$1';

describe('$1', () => {
  it('renders without crashing', () => {
    render(<$1 prop1="test" />);
  });

  it('displays correct content', () => {
    render(<$1 prop1="test" />);
    expect(screen.getByText(/test/i)).toBeInTheDocument();
  });
});
```

### 4. Storybook Story (if using Storybook)

```jsx
// src/components/$1.stories.jsx
import { $1 } from './$1';

export default {
  title: 'Components/$1',
  component: $1,
};

export const Default = {
  args: {
    prop1: 'Example',
  },
};
```

### 5. Documentation

Add to component README:
```markdown
## $1

Description of component.

**Props**:
- `prop1` (string, required): Description
- `prop2` (function): Description

**Example**:
\```jsx
<$1 prop1="value" />
\```
```

Provide all files ready to use.
```

**Usage**:
```
/gen-component UserProfile
```

---

## Example 4: Database Model Generator

**File**: `.claude/commands/gen-model.md`

```markdown
---
description: Generate database model with migrations
allowed-tools: Read, Grep, Glob, Write
argument-hint: [model-name]
---

## Existing Models

@src/models/User.js
@src/models/Post.js

## Database Conventions

@CLAUDE.md
@docs/database-schema.md

## Generation Task

Create database model: $1

### 1. Model Definition

```javascript
// src/models/$1.js
const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const $1 = sequelize.define('$1', {
  id: {
    type: DataTypes.UUID,
    defaultValue: DataTypes.UUIDV4,
    primaryKey: true,
  },
  // Add fields here
  createdAt: {
    type: DataTypes.DATE,
    allowNull: false,
  },
  updatedAt: {
    type: DataTypes.DATE,
    allowNull: false,
  },
});

// Associations
$1.associate = (models) => {
  // Define associations
};

module.exports = $1;
```

### 2. Migration

```javascript
// migrations/YYYYMMDDHHMMSS-create-$1.js
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('$1s', {
      id: {
        type: Sequelize.UUID,
        defaultValue: Sequelize.UUIDV4,
        primaryKey: true,
      },
      // Fields
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
    });

    // Add indexes
    await queryInterface.addIndex('$1s', ['field']);
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('$1s');
  },
};
```

### 3. Validation & Hooks

```javascript
// Add to model
$1.beforeCreate(async (instance) => {
  // Pre-create logic
});

$1.prototype.toJSON = function () {
  const values = Object.assign({}, this.get());
  // Hide sensitive fields
  delete values.password;
  return values;
};
```

### 4. Tests

```javascript
// tests/models/$1.test.js
describe('$1 Model', () => {
  it('creates instance with valid data', async () => {});
  it('validates required fields', async () => {});
  it('enforces constraints', async () => {});
});
```

Provide all files ready to integrate.
```

**Usage**:
```
/gen-model Notification
```

---

## Example 5: Documentation Generator

**File**: `.claude/commands/gen-docs.md`

```markdown
---
description: Generate documentation from code
allowed-tools: Read, Grep, Glob, Write
argument-hint: [file-or-directory]
---

## Code to Document

@$1

## Existing Documentation Style

@docs/api-reference.md

## Documentation Task

Generate comprehensive documentation for @$1:

### 1. Overview

```markdown
# [Module Name]

Brief description of what this module does.

## Purpose

Why this exists and when to use it.

## Key Concepts

Important concepts to understand.
```

### 2. API Reference

For each exported function/class:

```markdown
### functionName(param1, param2)

Description of what this function does.

**Parameters**:
- `param1` (type): Description
- `param2` (type, optional): Description. Default: value

**Returns**: (type) Description

**Throws**:
- `ErrorType`: When error occurs

**Example**:
\```javascript
const result = functionName('value', 42);
\```
```

### 3. Usage Examples

```markdown
## Usage

### Basic Example

\```javascript
// Common use case
\```

### Advanced Example

\```javascript
// Complex scenario
\```
```

### 4. Notes Section

```markdown
## Notes

- Important considerations
- Performance implications
- Thread safety
- Known limitations
```

Provide complete documentation ready to publish.
```

**Usage**:
```
/gen-docs src/utils/
```

---

## Example 6: Boilerplate Generator

**File**: `.claude/commands/gen-boilerplate.md`

```markdown
---
description: Generate boilerplate code for common patterns
allowed-tools: Read, Grep, Glob, Write
argument-hint: [pattern-type] [name]
---

## Pattern Templates

@templates/

## Project Conventions

@CLAUDE.md

## Generation Task

Generate $1 boilerplate named $2:

### Available Patterns

**crud-api**: Complete CRUD API endpoint
**service-class**: Service class with error handling
**react-form**: Form with validation
**middleware**: Express middleware
**util-function**: Utility function with tests
**async-handler**: Async operation handler

### Output

Complete, working boilerplate following project patterns:

1. **Main file**: Implementation
2. **Tests**: Unit tests
3. **Documentation**: Usage docs
4. **Types** (if TypeScript): Type definitions

All files ready to customize and use.
```

**Usage**:
```
/gen-boilerplate crud-api products
```

---

## Implementation Tips

1. **Reference existing patterns**
   ```markdown
   @src/examples/good-pattern.js
   ```

2. **Include multiple file types**
   - Implementation
   - Tests
   - Documentation
   - Configuration

3. **Make it ready-to-use**
   - Complete, working code
   - Not just snippets
   - Follows project conventions

4. **Provide customization guidance**
   - What to change
   - What to keep
   - Common customizations

5. **Test generated code**
   - Ensure it runs
   - Passes linting
   - Follows standards

---

These commands accelerate development while maintaining consistency!
